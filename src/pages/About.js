import React from "react";
import "./About.css";

const About = () => {
  return (
    <div className="about-container">
      <div className="about-card">
        <h1 className="about-title">About Mindly</h1>
        <p className="about-description">
          Mindly is a comprehensive platform dedicated to promoting mental health awareness and providing resources to enhance emotional well-being. 
          Our mission is to make mental health support accessible and approachable for everyone. 
          Whether you're seeking breathing exercises, helpline numbers, or engaging blogs to boost your mental wellness, Mindly has you covered.
        </p>
        <p className="about-vision">
          At Mindly, we believe mental health is as important as physical health. 
          Our platform integrates cutting-edge technologies and a user-friendly interface to make support and guidance readily available at your fingertips.
        </p>
        <p className="about-credit">
          Website Created by: <strong>Umangi Nigam,Tushar Swanskar</strong>

        </p>
      </div>
    </div>
  );
};

export default About;
