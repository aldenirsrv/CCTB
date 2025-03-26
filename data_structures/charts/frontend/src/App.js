import React, { useEffect, useState, useRef } from 'react';

import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './components/pages/home';
import CoinDetailPage from './components/pages/coinPageInfo';
import PageHeader from './_generic/page-header';

const App = () => {
  return (
    <Router>
      <PageHeader />
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/coin/:id" element={<CoinDetailPage />} />
      </Routes>
    </Router>
  );
};
export default App;