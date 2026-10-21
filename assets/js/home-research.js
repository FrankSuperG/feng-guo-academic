document.querySelectorAll("[data-publication-chart]").forEach((chart) => {
  const buttons = [...chart.querySelectorAll("[data-chart-mode]")];
  const years = [...chart.querySelectorAll("[data-year]")];
  const legend = chart.querySelector("[data-chart-legend]");
  buttons.forEach((button) => {
    button.addEventListener("click", () => {
      const mode = button.dataset.chartMode;
      const maximum = Math.max(1, ...years.map((year) => Number(year.dataset[mode])));
      buttons.forEach((item) => item.setAttribute("aria-pressed", String(item === button)));
      years.forEach((year) => {
        const value = Number(year.dataset[mode]);
        year.querySelector(".publication-chart__bar").style.height = `${(value / maximum) * 100}%`;
        year.querySelector(".publication-chart__value").textContent = value;
        const label = `${year.dataset.year}: ${value} ${mode === "cumulative" ? "cumulative " : ""}papers`;
        year.setAttribute("aria-label", label);
        year.title = label;
      });
      legend.textContent = mode === "cumulative" ? "Cumulative papers" : "Papers by publication year";
      chart.querySelector("ol").setAttribute("aria-label", legend.textContent);
    });
  });
});
