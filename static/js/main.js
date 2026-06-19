// ======================================
// Gesture Dashboard Controller
// ======================================

document.addEventListener("DOMContentLoaded", () => {

  const startBtn = document.getElementById("startBtn");
  const stopBtn = document.getElementById("stopBtn");
  const statusEl = document.getElementById("systemStatus");

  // ---------------- STATUS UI ----------------
  function setStatus(running){
    if(!statusEl) return;

    if(running){
      statusEl.textContent = "Running";
      statusEl.classList.remove("status-off");
      statusEl.classList.add("status-on");
    } else {
      statusEl.textContent = "Stopped";
      statusEl.classList.remove("status-on");
      statusEl.classList.add("status-off");
    }
  }

  // ---------------- START ----------------
  startBtn?.addEventListener("click", async () => {
    startBtn.disabled = true;
    await fetch("/start", { method: "POST" });
    setStatus(true);
    startBtn.disabled = false;
  });

  // ---------------- STOP ----------------
  stopBtn?.addEventListener("click", async () => {
    stopBtn.disabled = true;
    await fetch("/stop", { method: "POST" });
    setStatus(false);
    stopBtn.disabled = false;
  });

  // ---------------- AUTO STATUS CHECK ----------------
  async function syncStatus(){
    try{
      const res = await fetch("/status");
      const data = await res.json();
      setStatus(data.running);
    } catch(e){}
  }

  setInterval(syncStatus, 3000);
  syncStatus();

});

// ---------------- CALIBRATION ----------------
function applyCalibration(){
  const speed = document.getElementById("speed").value;
  const pinch = document.getElementById("pinch").value;

  fetch("/calibrate",{
    method:"POST",
    headers:{ "Content-Type":"application/json" },
    body: JSON.stringify({
      speed: speed,
      pinch: pinch
    })
  });
}
