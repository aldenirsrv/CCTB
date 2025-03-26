import React from 'react';
import { Bar } from 'react-chartjs-2';
import {MiniIndicatorHeader} from '../widgets'
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
  Filler
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

function BarChart({ data, timeData }) {
  // Check dark mode context
  const { isDarkMode } = useDarkMode()

  const textColor = isDarkMode ? '#fff' : '#000';
  const backgroundColor = isDarkMode ? 'rgba(75, 192, 192, 0.2)' : 'rgba(54, 162, 235, 0.2)';

  // Create gratient to chart
  const createGradient = (chart) => {
    const ctx = chart.chart.ctx;
    const gradient = ctx.createLinearGradient(0, 0, 0, chart.chart.height);
    if(chart.raw > 0) {
      gradient.addColorStop(0, 'rgba(15, 229, 161, 0.7)');
      gradient.addColorStop(1, 'rgba(15, 229, 161, 0)');
    } else {
      gradient.addColorStop(0, 'rgba(251, 71, 17, 0)');
      gradient.addColorStop(1, 'rgba(251, 72, 17, 0.5)');
    }
    return gradient;
  };

  // Border color based on current price  
  const createline = (chart) => {
    const ctx = chart.chart.ctx;
    if(chart.raw > 0) {
      return 'rgba(15, 229, 161, 1)'
    } else {
      return 'rgba(251, 72, 17, 1)';
    }
  };


  
  // Bar chart
  
  const barData = {
    labels: timeData,
    datasets: [
      {
        label: 'Comparator',
        data: data,
        backgroundColor: (chart) => createGradient(chart), 
        borderColor:(chart) => createline(chart),
        borderWidth: 1,
      },
    ],
  };
  const barOptions = {
    responsive: true,
       layout:{
          backgroundColor: backgroundColor
    },
    scales: {
      x: {
        title: {
          display: true,
          text: 'Tickers',
        },
      },
      y: {
        title: {
          display: true,
          text: 'Dwn / UP',
        },
        ticks: {
          beginAtZero: false,
          color: textColor 
        },
      },
    },
    plugins: {
      title: {
        display: true,
        text: 'Indicator',
        color: textColor 
      },
      legend: {
        display: true,
        position: 'top', //(options: 'top', 'left', 'bottom', 'right')
        labels: {
          color: textColor,
        },
      },
    },
    animation: {
      duration: 300,
      easing: 'cubic-in-out',
    },
  };

  return <div className={isDarkMode ? " dark-mode":"canvas-container light"} >
    <Bar className={isDarkMode ? 'charts-area dark-mode': 'charts-area'} data={barData} options={barOptions} />
</div>
}

export default BarChart;