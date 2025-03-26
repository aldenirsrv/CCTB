import React, { useState } from 'react';
import './ToggleButton.css';

const ToggleButton = ({ onClick }) => {
  const [isDarkMode, setIsDarkMode] = useState(false);

  const toggleDarkMode = () => {
    setIsDarkMode(prev => !prev);
    if (onClick) onClick();
  };

  return (
    <button 
      onClick={toggleDarkMode} 
      className={`toggle-button ${isDarkMode ? 'dark' : 'light'}`}
    >
      <div className={`slider ${isDarkMode ? 'dark' : 'light'}`}>
        <svg
          className="switch-icon"
          viewBox="0 0 27 27"
          xmlns="http://www.w3.org/2000/svg"
          style={{ display: isDarkMode ? 'none' : 'block' }}
        >
          <path
            fillRule="evenodd"
            clipRule="evenodd"
            d="M10.5 2h3v3h-3V2zM16 12a4 4 0 11-8 0 4 4 0 018 0zM5.99 3.869L3.867 5.99 5.99 8.112 8.111 5.99 5.989 3.87zM2 13.5v-3h3v3H2zm1.868 4.51l2.121 2.12 2.122-2.12-2.122-2.122-2.121 2.121zM13.5 19v3h-3v-3h3zm4.51-3.112l-2.121 2.122 2.121 2.121 2.121-2.121-2.121-2.122zM19 10.5h3v3h-3v-3zm-3.11-4.51l2.12 2.121 2.122-2.121-2.121-2.121-2.122 2.121z"
            fill={isDarkMode ? '#000' : '#fff' }
          ></path>
        </svg>
        <svg
          className="switch-icon"
          viewBox="0 0 27 27"
          xmlns="http://www.w3.org/2000/svg"
          style={{ display: !isDarkMode ? 'none' : 'block' }}
        >
          <path
            d="M20.968 12.768a7 7 0 01-9.735-9.735 9 9 0 109.735 9.735z"
            fill={isDarkMode ? '#000' : '#fff' }
          ></path>
        </svg>
      </div>
    </button>
  );
};

export default ToggleButton;