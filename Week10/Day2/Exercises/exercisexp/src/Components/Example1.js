import React from "react";

const Example1 = ({ data }) => {
  const { SocialMedias } = data;

  return (
    <div>
      <h2>Social Medias</h2>
      {SocialMedias.map((media, index) => (
        <div key={index}>
          <p>URL: {media}</p>
        </div>
      ))}
    </div>
  );
};

export default Example1;
