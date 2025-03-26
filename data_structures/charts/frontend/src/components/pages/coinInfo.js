import React from 'react';
import './style.css';
import { Link } from 'react-router-dom';
import { useDarkMode } from '../../_generic/dark-mode.js';

const CoinInfo = ({ coinData }) => {
  const { name, symbol, description, categories, links, image } = coinData;
  const { isDarkMode } = useDarkMode()

  return (
    <div className={isDarkMode ? "coin-container dark-mode": "coin-container light"}>
      <div className='section-info'>
        <div className="breadcrumb">
            <Link to="/">Home</Link> &gt; <span>{coinData.name}</span>
          </div>
          <div className="coin-header">
            <img src={image.large} alt={name} className="coin-logo" />
            <h1 className="coin-name">{name} ({symbol.toUpperCase()})</h1>
          </div>

          <p className="coin-description">{description.en}</p>

          {/* Additional Information */}
          <div className="additional-info">
            <h3>Additional Information</h3>
            <p><strong>Genesis Date:</strong> {coinData.genesis_date}</p>
            <p><strong>Positive Sentiment:</strong> {coinData.sentiment_votes_up_percentage}%</p>
            <p><strong>Negative Sentiment:</strong> {coinData.sentiment_votes_down_percentage}%</p>
            <p><strong>Watchlist Users:</strong> {coinData.watchlist_portfolio_users}</p>
            <p><strong>Market Rank:</strong> {coinData.market_cap_rank}</p>
          </div>

          <h2>Categories</h2>
          <ul className="category-list">
            {categories.map((category, index) => (
              <li key={index} className="category-item">{category}</li>
            ))}
          </ul>

          <div className="links-section">
            <div>
              <h3>Links</h3>
              <a href={links.homepage[0]} className="link-button" target="_blank" rel="noopener noreferrer">Official Website</a>
            </div>

            <div>
              <h3>Social</h3>
              <div className="social-icons">
                <a href={`https://twitter.com/${links.twitter_screen_name}`} target="_blank" rel="noopener noreferrer">Twitter</a>
                <a href={`https://www.facebook.com/${links.facebook_username}`} target="_blank" rel="noopener noreferrer">Facebook</a>
                <a href={links.subreddit_url} target="_blank" rel="noopener noreferrer">Reddit</a>
              </div>
            </div>
          </div>
    </div>
  </div>
    
  );
};

export default CoinInfo;