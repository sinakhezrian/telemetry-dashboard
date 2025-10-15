function change_status(status) {
  const statusIndicator = document.getElementById("status-indicator");
  const statusText = document.getElementById("status-text");

  if (status) {
    statusIndicator.classList.remove("bg-red-500");
    statusIndicator.classList.add("bg-green-500");
    statusText.textContent = "Connected";
  } else {
    statusIndicator.classList.remove("bg-green-500");
    statusIndicator.classList.add("bg-red-500");
    statusText.textContent = "Disconnected";
  }
}

() => {
  change_status(true);
};
