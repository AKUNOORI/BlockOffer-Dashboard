import React, { useState } from 'react';
import axios from 'axios';
import './index.css'; 
import { Navigate } from 'react-router-dom';
import { Chart } from 'react-google-charts';

const PostData = () => {
    const [formData, setFormData] = useState({
        end_year: '',
        topic: '',
        sector: '',
        region: '',
        pestle: '',
        source: '',
        country: ''
    });
    const [responseData, setResponseData] = useState([]);
    const [error, setError] = useState(null);
    const [auth, setAuth] = useState(false);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name]: name === 'end_year' ? value.toString() : value
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        console.log('form submit data', formData);
        try {
            const response = await axios.post('http://localhost:8000/api/visualization/', formData, {
                headers: {
                    'Content-Type': 'application/json'
                }
            });
            console.log(response.data.data);
            setResponseData(response.data.data);
        } catch (error) {
            setError(error.response ? error.response.data : "Error: Unable to connect to the server");
        }
    };

      const [filter, setFilter] = useState({ country: '', topic: '' });

      const filteredData = responseData.filter(item => {
        return (
          (filter.country === '' || item.country === filter.country) &&
          (filter.topic === '' || item.topic === filter.topic)
        );
      });

      const countryShortcuts = {
        "United States of America": "USA",
        "Mexico": "MEX",
        "Nigeria": "NGA",
        "United Kingdom": "UK",
      };
      
      const data = [
        ['Country', 'Intensity', 'Likelihood', 'Relevance', 'Region', 'Start_year', 'Topic'],
        ...filteredData.map(item => [
          countryShortcuts[item.country] || item.country,
          item.intensity,
          item.likelihood,
          item.relevance,
          item.region,
          item.start_year,
          item.topic
        ])
      ];
    

      const options = {
        title: 'Intensity, Likelihood, and Relevance by Country',
        chartArea: { width: '50%' },
        hAxis: {
          title: 'Value',
          minValue: 0,
        },
        vAxis: {
          title: 'Country',
        },
        seriesType: 'bars',
      };

    return (
        <div>
           <div className='main-form'>
           <form onSubmit={handleSubmit}>
            <div className="form">
                <div>
                    <label>End Year:</label>
                    <input type="text" name="end_year" value={formData.end_year} onChange={handleChange}  />
                </div>
                <div>
                    <label>Topic:</label>
                    <input type="text" name="topic" value={formData.topic} onChange={handleChange}  />
                </div>
                <div>
                    <label>Sector:</label>
                    <input type="text" name="sector" value={formData.sector} onChange={handleChange}     />
                </div>
                <div>
                    <label>Region:</label>
                    <input type="text" name="region" value={formData.region} onChange={handleChange}  />
                </div>
                <div>
                    <label>Pestle:</label>
                    <input type="text" name="pestle" value={formData.pestle} onChange={handleChange}  />
                </div>
                <div>
                    <label>Source:</label>
                    <input type="text" name="source" value={formData.source} onChange={handleChange}  />
                </div>
                <div>
                    <label>Country:</label>
                    <input type="text" name="country" value={formData.country} onChange={handleChange}  />
                </div>
                </div>
                <button className='submitbtn' type="submit">Fetch Data</button>
            </form>
            {error && <div className="error">Error: {JSON.stringify(error)}</div>}

           </div>
           <div>

                        {(Array.isArray(responseData) && responseData.length > 0 ) ? (
                    <div >
                        <Chart
                            className='chart-bar'
                            chartType="Bar"
                            width="100%"
                            height="580px"
                            data={data}
                            options={options}
                        />
                    </div>
                ):
                (<div className='chart-info-text'>No data found, Please choose filters...</div>)}
           </div>
            
           
        </div>
    );
};

export default PostData;
