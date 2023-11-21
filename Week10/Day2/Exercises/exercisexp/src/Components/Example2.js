import React from "react";

const Example2 = ({ data }) => {
  const { Skills } = data;

  return (
    <div>
      <h2>Skills</h2>
      {Skills.map((skillArea, index) => (
        <div key={index}>
          <h3>{skillArea.Area}</h3>
          <ul>
            {skillArea.SkillSet.map((skill, skillIndex) => (
              <li key={skillIndex}>
                {skill.Name} - {skill.Hot ? "Hot" : "Not Hot"}
              </li>
            ))}
          </ul>
        </div>
      ))}
    </div>
  );
};

export default Example2;
