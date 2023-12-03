document.getElementById('checkUrlButton').addEventListener('click', function() {
  chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
      // Send a message to the background script to check the URL
      chrome.runtime.sendMessage({action: "checkUrl", tabId: tabs[0].id}, function(response) {
          // Update the popup based on the response
          if (response.urlInDatabase) {
              document.getElementById('result').textContent = 'This URL is in the database.';
          } else {
              document.getElementById('result').textContent = 'This URL is not in the database.';
          }
      });
  });
});