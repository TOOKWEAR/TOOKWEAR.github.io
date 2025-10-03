async function loadStatus() {
  try {
    const res = await fetch("/api/status");
    const data = await res.json();

    if (data.online) {
      document.getElementById("server-status").textContent = "✅ Online";
      document.getElementById("player-count").textContent =
        `Players: ${data.players} / ${data.max}`;
    } else {
      document.getElementById("server-status").textContent = "❌ Offline";
    }
  } catch {
    document.getElementById("server-status").textContent = "API nicht erreichbar";
  }
}

loadStatus();
setInterval(loadStatus, 30000);