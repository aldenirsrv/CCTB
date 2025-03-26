import React from 'react';
import { Line } from 'react-chartjs-2';
import ChartHeader from '../widgets/chart-header'
import { useDarkMode } from '../../_generic/dark-mode';
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement,
  BarElement,
  ArcElement,
  Filler,
  layout
} from 'chart.js';

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement,
  BarElement,
  ArcElement,
  Filler
);
function LineChart({ data, timeData, details }) {
  // Check dark mode context
  const { isDarkMode } = useDarkMode()

  const textColor = isDarkMode ? '#fff' : '#000';
  const gridColor = isDarkMode ? 'rgba(255, 255, 255, 0.2)' : 'rgba(0, 0, 0, 0.1)';
  const backgroundColor = isDarkMode ? 'rgba(75, 192, 192, 0.2)' : 'rgba(54, 162, 235, 0.2)';
  const borderColor = isDarkMode ? 'rgba(75, 192, 192, 1)' : 'rgba(54, 162, 235, 1)';
  
  // Create gratient to chart
  const createGradient = (chart) => {
    const ctx = chart.chart.ctx;
    const gradient = ctx.createLinearGradient(0, 0, 0, chart.chart.height);
    if  (details?.data?.percent > 0) {
      gradient.addColorStop(0, 'rgba(15, 229, 161, 0.2)');
      gradient.addColorStop(1, 'rgba(15, 229, 161, 0)');
    } else {
      gradient.addColorStop(0, 'rgba(251, 72, 17, 0.2)');
      gradient.addColorStop(1, 'rgba(251, 72, 17, 0)');
    }
   
    return gradient;
  };

  const lineOptions = {
    responsive: true,
    scales: {
      x: {
        display: true,
        grid: {
          display: false,
        },
        ticks: {
          color: textColor,
        },
      },
      y: {
        title: {
          display: true,
          text: 'Price (USD)',
        },
        ticks: {
          color: textColor,
        },
        grid: {
          display: true,
          color: gridColor,
          drawBorder: true,
          borderColor: borderColor,
        },
      },
    },
    elements: {
      line: {
        backgroundColor: 'rgb(15, 229, 161)',
      },
    },
    plugins: {
      title: {
        display: false,
        text: 'Price do Bitcoin',
      },
      tooltip: {
        color: textColor,
      },
      legend: {
        display: true,
        position: 'top',
        labels: {
          color: textColor,
        },
      },
    },
    layout: {
      backgroundColor: backgroundColor,
    },
    animation: {
      duration: 300,
      easing: 'cubic-in-out',
    },
  };
  const btcData = {
    labels: timeData.map((timestamp) =>
      new Date(timestamp * 1000).toLocaleTimeString()
    ),
    datasets: [
      {
        label: details?.crypto_id || "loading...",
        data: data,
        fill: true,
        borderColor: details?.data?.percent > 0 ? 'rgb(15, 229, 161)' :'rgba(251, 72, 17, 1)' ,
        backgroundColor: (chart) => createGradient(chart),
        borderWidth: 2,
        tension: 0.4,
        pointRadius: 5,
        pointBackgroundColor: details?.data?.percent > 0 ? 'rgb(15, 229, 161)' :'rgba(251, 72, 17, 1)' ,
        pointBorderColor: 'white',
        pointBorderWidth: 2,
        showLine: true,
      },
    ],
  };

  return <div className={isDarkMode ? " dark-mode":"canvas-container light"} >
    <ChartHeader data={details}/>
    <Line className={isDarkMode ? 'charts-area dark-mode': 'charts-area'} data={btcData} options={lineOptions} />
  </div>;
}

export default LineChart;