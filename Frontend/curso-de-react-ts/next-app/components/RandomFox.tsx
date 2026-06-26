import React from "react";

type Props = { imageUrl: string };

export const RandomFox = ({ imageUrl }: Props ): React.JSX.Element => {
    return <img src={ imageUrl }  alt="Fox image" width={320} height="auto" className="rounded-lg"/>;
};
