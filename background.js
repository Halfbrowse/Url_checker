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
                let message = `This site is ${data.summary} and has an attribution confidence level of ${data.attribution_confidence}`;
                chrome.scripting.executeScript({
                    target: { tabId: tabId },
                    func: displayMessage,
                    args: [message]
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
  