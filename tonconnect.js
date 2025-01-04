// Kiểm tra xem SDK có tạo biến TonConnectSDK không
console.log("TonConnectSDK:", window.TonConnectSDK);

// Khởi tạo SDK
const connector = new TonConnectSDK(); 

// Ví dụ: gắn hàm connectWallet
async function connectWallet() {
  try {
    console.log("Connect Wallet clicked!");
    await connector.connectWallet();
    alert("Wallet connected!");
    document.getElementById("connectBtn").style.display = "none";
    document.getElementById("openBtn").style.display = "inline-block";
  } catch (err) {
    console.error("Failed to connect wallet:", err);
  }
}

// Ví dụ: gắn hàm openBox
async function openBox() {
  try {
    await connector.sendTransaction({ to: "SOME_ADDRESS", value: "1000000000" });
    alert("Payment successful!");
    document.getElementById("rewardBox").style.display = "block";
    document.getElementById("rewardBox").textContent = "You got a Frost Phoenix!";
  } catch (err) {
    console.error("Payment failed:", err);
  }
}

// Gắn các sự kiện nếu phần tử HTML tồn tại
window.addEventListener("DOMContentLoaded", () => {
  const btnConnect = document.getElementById("connectBtn");
  const btnOpen = document.getElementById("openBtn");
  if (btnConnect) {
    btnConnect.addEventListener("click", connectWallet);
  }
  if (btnOpen) {
    btnOpen.addEventListener("click", openBox);
  }
});
