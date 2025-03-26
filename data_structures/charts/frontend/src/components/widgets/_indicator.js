import React from 'react';

function Indicador({ percent=0, small = false }) {
  return  <div className={Number(percent) >= 0 ? 'indicador green' : ' indicador red'}>
           <div>
                <span hidden={small}>
                    {Number(percent)> 0 ? '⬆' : '⬇'}
                </span>
            </div>
            <span>
                {percent}%
            </span>
        </div>;
}

export default Indicador;