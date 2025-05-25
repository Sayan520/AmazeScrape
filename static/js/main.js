document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("scrapeForm");
  const spinner = document.getElementById("loadingSpinner");
  const submitBtn = form.querySelector('button[type="submit"]');
  const progressContainer = document.getElementById("progressContainer");
  const progressBar = document.getElementById("progressBar");

  // toast container for notifications
  function showToast(message, type = "success") {
    const toastContainer = document.getElementById("toastContainer");
    const toast = document.createElement("div");
    toast.className = `toast ${type}`;
    toast.textContent = message;
    toastContainer.appendChild(toast);

    setTimeout(() => {
      toast.remove();
    }, 4000);
  }

  // Update progress bar
  function updateProgress(current, total) {
    const percent = Math.round((current / total) * 100);
    progressContainer.classList.remove("hidden");
    progressBar.style.width = percent + "%";
  }

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    // Reset progress bar and spinner
    const query = form.query.value.trim();
    const pages = parseInt(form.pages.value, 10);
    const format = form.format.value;
    const filename = form.filename.value.trim() || "output";

    if (!query || isNaN(pages) || pages < 1) {
      showToast("Please enter a valid query and number of pages.", "error");
      return;
    }

    // Show confirmation modal before scraping
    Swal.fire({
      title: "Start scraping?",
      text: `Scrape ${pages} page(s) for "${query}" and download as ${format.toUpperCase()}?`,
      icon: "question",
      showCancelButton: true,
      confirmButtonText: "Yes, scrape it!",
      cancelButtonText: "Cancel",
    }).then(async (result) => {
      if (!result.isConfirmed) return;

      const payload = { query, pages, format, filename };

      submitBtn.disabled = true;
      spinner.classList.remove("hidden");
      progressContainer.classList.add("hidden");
      progressBar.style.width = "0%";

      try {
        const response = await fetch("/api/scrape", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(payload),
        });

        if (!response.ok) {
          const err = await response.json();
          throw new Error(err.error || "Unknown error occurred");
        }

        // Simulated progress update (for demo — replace with real logic if backend supports)
        for (let i = 1; i <= pages; i++) {
          updateProgress(i, pages);
          await new Promise((r) => setTimeout(r, 300)); // simulate page scrape delay
        }

        const disposition = response.headers.get("Content-Disposition");
        let downloadFilename = filename + (format === "csv" ? ".csv" : ".xlsx");

        const match = disposition?.match(
          /filename\*?=['"]?(?:UTF-8'')?([^'";\n]+)/i
        );
        if (match && match[1]) {
          downloadFilename = decodeURIComponent(match[1]);
        }

        // download update format preview
        const formatSelect = document.getElementById("format");
        const filenameInput = document.getElementById("filename");
        const previewEl = document.getElementById("formatPreview");

        function updatePreview() {
          const format = formatSelect.value;
          const name = filenameInput.value.trim() || "output";
          let desc =
            format === "csv" ? "(Comma Separated)" : "(Microsoft Excel)";
          previewEl.textContent = `${name}.${format} ${desc}`;
        }

        formatSelect.addEventListener("change", updatePreview);
        filenameInput.addEventListener("input", updatePreview);
        updatePreview(); // initial preview update

        // Download the file
        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url;
        a.download = downloadFilename;
        document.body.appendChild(a);
        a.click();
        a.remove();
        window.URL.revokeObjectURL(url);

        showToast("Scraping complete. File downloaded.", "success");
      } catch (error) {
        console.error(error);
        showToast("Error: " + error.message, "error");
      } finally {
        spinner.classList.add("hidden");
        submitBtn.disabled = false;
      }
    });
  });
});
