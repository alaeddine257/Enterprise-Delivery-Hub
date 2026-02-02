const initTableSearch = () => {
  document.querySelectorAll("[data-table-search]").forEach((input) => {
    const targetSelector = input.getAttribute("data-table-search");
    const table = document.querySelector(targetSelector);
    if (!table) return;

    input.addEventListener("input", (event) => {
      const query = event.target.value.toLowerCase();
      table.querySelectorAll(".table-row").forEach((row) => {
        if (row.classList.contains("table-header")) return;
        const text = row.textContent.toLowerCase();
        row.style.display = text.includes(query) ? "grid" : "none";
      });
    });
  });
};

const initRealtimeSummary = () => {
  const cards = document.querySelectorAll("[data-kpi]");
  if (!cards.length) return;

  const refresh = async () => {
    try {
      const response = await fetch("/api/summary");
      if (!response.ok) return;
      const payload = await response.json();

      document.querySelectorAll("[data-kpi-total]").forEach((el) => {
        el.textContent = payload.projects?.total ?? 0;
      });
      document.querySelectorAll("[data-kpi-backlog]").forEach((el) => {
        el.textContent = payload.projects?.backlog ?? 0;
      });
      document.querySelectorAll("[data-kpi-inprogress]").forEach((el) => {
        el.textContent = payload.projects?.in_progress ?? 0;
      });
      document.querySelectorAll("[data-kpi-atrisk]").forEach((el) => {
        el.textContent = payload.projects?.at_risk ?? 0;
      });
      document.querySelectorAll("[data-kpi-closed]").forEach((el) => {
        el.textContent = payload.projects?.closed ?? 0;
      });
      document.querySelectorAll("[data-kpi-tasks]").forEach((el) => {
        el.textContent = payload.tasks?.total ?? 0;
      });
      document.querySelectorAll("[data-kpi-blocked]").forEach((el) => {
        el.textContent = payload.tasks?.blocked ?? 0;
      });
      document.querySelectorAll("[data-kpi-done]").forEach((el) => {
        el.textContent = payload.tasks?.done ?? 0;
      });
      document.querySelectorAll("[data-kpi-openrisks]").forEach((el) => {
        el.textContent = payload.risks?.open ?? 0;
      });
    } catch (error) {
      console.error("Summary refresh failed", error);
    }
  };

  refresh();
  setInterval(refresh, 30000);
};

const initFormHints = () => {
  document.querySelectorAll("form").forEach((form) => {
    form.addEventListener("submit", () => {
      const button = form.querySelector("button[type='submit']");
      if (button) {
        button.dataset.originalText = button.textContent;
        button.textContent = "Saving...";
        button.disabled = true;
      }
    });
  });
};

const initHighlightRows = () => {
  document.querySelectorAll(".table-row").forEach((row) => {
    const status = row.querySelector(".status");
    if (!status) return;
    if (status.textContent.includes("At Risk") || status.textContent.includes("Blocked")) {
      row.classList.add("row-alert");
    }
  });
};

const initClock = () => {
  const target = document.querySelector("[data-clock]");
  if (!target) return;
  const update = () => {
    const now = new Date();
    target.textContent = now.toLocaleString();
  };
  update();
  setInterval(update, 1000 * 60);
};

document.addEventListener("DOMContentLoaded", () => {
  initTableSearch();
  initRealtimeSummary();
  initFormHints();
  initHighlightRows();
  initClock();
});
