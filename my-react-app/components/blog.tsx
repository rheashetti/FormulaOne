import React from 'react';
import './blog.css';

const Blog = () => {

    const recaps = [
        { id: 1, title:'Recap 1', content: 'This is the first recap' },
        { id: 2, title:'Recap 2', content: 'This is the second recap' },
        { id: 3, title:'Recap 3', content: 'This is the third recap' },
        { id: 4, title:'Recap 4', content: 'This is the fourth recap' },
    ];

    const mostRecentRecap = recaps[recaps.length - 1];
    const otherRecaps = recaps.slice(0, recaps.length - 1);

    return (
        <div className="blog-container">
            <div className="most-recent-recap">
                <h2>{mostRecentRecap.title}</h2>
                <p>{mostRecentRecap.content}</p>
            </div>
            <div className="recaps-grid">
                {otherRecaps.map((recap) => (
                    <div key={recap.id} className="recap-card">
                        <h3>{recap.title}</h3>
                        <p>{recap.content}</p>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default Blog;