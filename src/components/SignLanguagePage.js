import React from "react";

function SignLanguagePage() {
  return (
    <div className="sign-language-page">
      <h1>Sign Language Translation</h1>
      <div className="camera-feed">
        {/* Use WebRTC or a library like react-webcam */}
        <p>Camera feed here (ML model integration required).</p>
      </div>
      <div className="output">
        <h3>Detected Gesture:</h3>
        <p>Gesture text will appear here...</p>
      </div>
    </div>
  );
}

export default SignLanguagePage;