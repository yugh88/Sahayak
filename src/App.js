import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import HomePage from "./components/HomePage";
import SignLanguagePage from "./components/SignLanguagePage";
import EnvironmentDetectionPage from "./components/EnvironmentDetectionPage";
import LanguageTranslationPage from "./components/LanguageTranslationPage";
import AboutPage from "./components/AboutPage";
import ContactPage from "./components/ContactPage";
import NavBar from "/Users/yughjuneja/Sahayak/src/components/NavBar.js";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/sign-language" element={<SignLanguagePage />} />
        <Route path="/environment-detection" element={<EnvironmentDetectionPage />} />
        <Route path="/language-translation" element={<LanguageTranslationPage />} />
        <Route path="/about" element={<AboutPage />} />
        <Route path="/contact" element={<ContactPage />} />
      </Routes>
    </Router>
  );
}

export default App;