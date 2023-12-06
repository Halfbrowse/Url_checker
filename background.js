chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
    if (changeInfo.status === 'complete' && tab.active) {
        checkUrl(tab.url, tabId);
    }
  });
  
  function checkUrl(url, tabId) {
    if (url.startsWith('chrome://')) {
        return;
    }
    fetch(`http://localhost:5000/check?url=${encodeURIComponent(url)}`)
        .then(response => response.json())
        .then(data => {
            if (data.exists) {
                chrome.scripting.executeScript({
                    target: { tabId: tabId },
                    func: displayMessage,
                    args: ["URL Found in Database"]
                });
            } 
        })
        .catch(error => {
            console.error('Error:', error);
        });
  }
  
  function displayMessage(message) {
    alert(message);
  }
  