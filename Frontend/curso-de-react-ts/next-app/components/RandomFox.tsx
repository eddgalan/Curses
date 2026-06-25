import React from "react";

export const RandomFox = (): React.JSX.Element => {
    const imageUrl = `https://randomfox.ca/images/${random()}.jpg`;

    return <img src={imageUrl}  alt="Fox image" width={320} height="auto" className="rounded-lg"/>;
};

const random = (): number => Math.floor(Math.random() * 123) + 1;

export default { RandomFox };
