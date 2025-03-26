import React, { useEffect, useState, useRef } from 'react';
import { useDarkMode } from './dark-mode';
import ToggleButton from '../components/widgets/_dark-mode-btn';


function PageHeader() {
    const { isDarkMode, toggleDarkMode } = useDarkMode()
  
  return (
    <div id='header' className={isDarkMode ? 'dark-mode': ''}>
    <div className="grid-title">
      <img className='logo' src='https://cryptologos.cc/logos/binance-usd-busd-logo.png?v=040' width={20} height={20} />
      <span className='logo-desc'> TUTOR | CRIPTO </span>
      <div>
      </div>
      <div className='right'>
        <span className='user'> John Doe</span>
        
         </div>
      <img className='user' src='https://demo-lucid-hugo.define.run/images/avatar.svg' />
      <ToggleButton onClick={toggleDarkMode} />
    </div>
    
   
    </div>
  );
}
export default PageHeader;