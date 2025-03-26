import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';

import axios from 'axios';
import CoinInfo from './coinInfo';

const CoinDetailPage = () => {

      const { id } = useParams();
      const [coinData, setCoinData] = useState(null); // Estado para armazenar os dados da moeda
      const [loading, setLoading] = useState(true); // Estado de carregamento
      const [error, setError] = useState(null); // Estado de erro
    
    
    
      useEffect(() => {
        const fetchCoinData = async () => {
          try {
            setLoading(true);
            const response = await axios.get(`http://localhost:8000/details?ticker=${id}`);
            setCoinData(response.data);
          } catch (err) {
            setError('Erro ao carregar os dados da moeda.');
          } finally {
            setLoading(false);
          }
        };
    
        fetchCoinData();
      }, [id]);
    
      if (loading) {
        return <h2>Carregando...</h2>;
      }
    
      if (error) {
        return <h2>{error}</h2>;
      }
    
      if (!coinData) {
        return <h2>DAta not found.</h2>;
      }
  return (
    <div>
      <CoinInfo coinData={coinData} />
    </div>
  );
};

export default CoinDetailPage;