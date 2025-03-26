package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"strings"

	"github.com/rs/cors"
)

const BASE_URL = "https://api.coingecko.com/api/v3"

// Data structures to store the API response
type Description struct {
	EN string `json:"en"`
}

type Links struct {
	Homepage          []string `json:"homepage"`
	Whitepaper        string   `json:"whitepaper"`
	BlockchainSite    []string `json:"blockchain_site"`
	OfficialForumURL  []string `json:"official_forum_url"`
	TwitterScreenName string   `json:"twitter_screen_name"`
	FacebookUsername  string   `json:"facebook_username"`
	SubredditURL      string   `json:"subreddit_url"`
	ReposURL          Repos    `json:"repos_url"`
}

type Repos struct {
	Github    []string `json:"github"`
	Bitbucket []string `json:"bitbucket"`
}

type Image struct {
	Thumb string `json:"thumb"`
	Small string `json:"small"`
	Large string `json:"large"`
}

type CoinInfo struct {
	ID                 string      `json:"id"`
	Symbol             string      `json:"symbol"`
	Name               string      `json:"name"`
	WebSlug            string      `json:"web_slug"`
	Categories         []string    `json:"categories"`
	Description        Description `json:"description"`
	Links              Links       `json:"links"`
	Image              Image       `json:"image"`
	CountryOrigin      string      `json:"country_origin"`
	GenesisDate        string      `json:"genesis_date"`
	SentimentVotesUp   float64     `json:"sentiment_votes_up_percentage"`
	SentimentVotesDown float64     `json:"sentiment_votes_down_percentage"`
	WatchlistPortfolio int         `json:"watchlist_portfolio_users"`
	MarketCapRank      int         `json:"market_cap_rank"`
}

func tickerDetails(w http.ResponseWriter, r *http.Request) {
	// Recupera o valor do parâmetro 'ticker' da URL
	ticker := r.URL.Query().Get("ticker")
	if ticker == "" {
		http.Error(w, "Ticker parameter is required", http.StatusBadRequest)
		return
	}

	// Remove "USDT" and convert to lowercase
	ticker = strings.Replace(ticker, "USDT", "", 1) // Remove "USDT" uma vez
	ticker = strings.ToLower(ticker)
	fmt.Println("Ticker:", ticker) // Converte para minúsculo

	// Mapping of symbol to currency ID
	symbolToID := map[string]string{
		"btc": "bitcoin",
		"eth": "ethereum",
		"xrp": "ripple",
		"sol": "solana",
		"mkr": "maker",
	}

	// Check if the symbol is valid
	id, exists := symbolToID[ticker]
	if !exists {
		http.Error(w, "Invalid symbol", http.StatusBadRequest)
		return
	}

	fmt.Println("Coin ID:", id)

	// Build the URL dynamically using the ticker
	url := fmt.Sprintf("https://api.coingecko.com/api/v3/coins/%s", id)
	print(url)
	// Making the HTTP request to the built URL
	resp, err := http.Get(url)
	if err != nil {
		http.Error(w, "Error accessing the CoinGecko API", http.StatusInternalServerError)
		return
	}
	defer resp.Body.Close()

	// Check if the API response is successful (status 200)
	if resp.StatusCode != http.StatusOK {
		http.Error(w, fmt.Sprintf("CoinGecko API returned an error: %s", resp.Status), http.StatusInternalServerError)
		return
	}

	// Initializing the variable where we will store the deserialized data
	var coinInfo CoinInfo

	// Deserializing the JSON response
	if err := json.NewDecoder(resp.Body).Decode(&coinInfo); err != nil {
		http.Error(w, "Error deserializing the response", http.StatusInternalServerError)
		return
	}

	// Set the response header as JSON
	w.Header().Set("Content-Type", "application/json")

	// Send the response as JSON
	if err := json.NewEncoder(w).Encode(coinInfo); err != nil {
		http.Error(w, "Error sending JSON response", http.StatusInternalServerError)
		return
	}
}

func healthz(w http.ResponseWriter, r *http.Request) {

	w.WriteHeader(200)
	w.Write([]byte("ok"))
}

func main() {
	// Configure CORS
	c := cors.New(cors.Options{
		AllowedOrigins:   []string{"*"}, // Permite todas as origens
		AllowedMethods:   []string{"GET", "POST", "PUT", "DELETE"},
		AllowedHeaders:   []string{"Content-Type", "Authorization"},
		AllowCredentials: true, // Caso precise de credenciais (cookies, etc.)
	})
	// Apply CORS to your route handler
	handlerWithCors := c.Handler(http.HandlerFunc(tickerDetails))

	// Endpoints
	http.Handle("/details", handlerWithCors)
	http.HandleFunc("/healthz", healthz)

	// Configure the server to listen on port 8000
	fmt.Println("Server started at http://localhost:8000")
	if err := http.ListenAndServe(":8000", nil); err != nil {
		fmt.Println("Error starting server:", err)
	}
}
