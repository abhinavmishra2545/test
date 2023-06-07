// Get the necessary DOM elements
const startBtn = document.getElementById('startBtn');
const transcription = document.getElementById('transcription');

// Create a new instance of SpeechRecognition
const recognition = new webkitSpeechRecognition();
recognition.interimResults = true; // Enable interim results for real-time transcription

// Event handler for the start button
startBtn.addEventListener('click', () => {
  recognition.start();
});

// Event handler for speech recognition results
recognition.onresult = (event) => {
  const result = event.results[event.results.length - 1];
  const transcript = result[0].transcript;

  // Display the interim or final transcription result
  if (result.isFinal) {
    transcription.value += transcript + '\n';
  } else {
    transcription.value = transcript;
  }
};

// Event handler for speech recognition errors
recognition.onerror = (event) => {
  console.error('Speech recognition error:', event.error);
};

