import React from "react";

type Props = { imageUrl: string };

export const RandomFox = ({ imageUrl }: Props ): React.JSX.Element => {
    return (
        <img src={ imageUrl }
             alt="Fox image"
             width={320}
             className="h-auto rounded-lg"
        />
    );
};
