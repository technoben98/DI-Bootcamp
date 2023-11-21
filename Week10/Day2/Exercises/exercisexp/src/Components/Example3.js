import React from "react";

const Example3 = ({ data }) => {
  const { Experiences } = data;

  return (
    <div>
      <h2>Experiences</h2>
      {Experiences.map((experience, index) => (
        <div key={index}>
          <img src={experience.logo} alt={experience.companyName} />
          <h3>{experience.companyName}</h3>
          <p>
            <a href={experience.url} target="_blank" rel="noopener noreferrer">
              {experience.url}
            </a>
          </p>
          {experience.roles.map((role, roleIndex) => (
            <div key={roleIndex}>
              <p>Title: {role.title}</p>
              <p>Description: {role.description}</p>
              <p>Start Date: {role.startDate}</p>
              <p>End Date: {role.endDate}</p>
              <p>Location: {role.location}</p>
            </div>
          ))}
        </div>
      ))}
    </div>
  );
};

export default Example3;
