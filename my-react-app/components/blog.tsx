import React from 'react';
import './blog.css';

import saudiaarabia from './recaps/5-saudiarabia.jpg';
import australia from './recaps/1-australia.jpg';
import china from './recaps/2-china.jpg';
import japan from './recaps/3-japan.jpg';
import bahrain from './recaps/4-bahrain.jpg';

const Blog = () => {

    const recaps = [
        { id: 5, title:'Recap 1', content:  saudiaarabia},
        { id: 4, title:'Recap 5', content: bahrain },
        { id: 3, title:'Recap 4', content: japan },
        { id: 2, title:'Recap 3', content: china },
        { id: 1, title:'Recap 2', content: australia },
    ];

    const otherRecaps = recaps;

    return (
        <div className="blog-container">
            <div className="recaps-grid">
                {otherRecaps.map((recap) => (
                    <div key={recap.id} className="recap-card">
                        {/* <h3>{recap.title}</h3> */}
                        <img src={recap.content} alt={recap.title} />
                    </div>
                ))}
            </div>
        </div>
    );
};

export default Blog;