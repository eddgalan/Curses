import React, { useEffect, useRef, useState } from "react";

type Props = { imageUrl: string };

export const RandomFox = ({ imageUrl }: Props ): React.JSX.Element => {
    const node = useRef<HTMLImageElement>(null);
    const [src, setSrc] = useState<string>("data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==");

    useEffect(() => {
        if (!node.current) return;

        // Create a new IntersectionObserver instance
        const observer = new IntersectionObserver(entries => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    setSrc(imageUrl);
                }
            });
        });

        // Start observing the target node
        observer.observe(node.current);

        // Stop observing the target node
        return () => {
            observer.disconnect();
        }
    }, [imageUrl]);

    return (
        <img src={ src }
             alt="Fox image"
             width={320}
             className="h-auto rounded-lg bg-gray-300"
             ref={node}
        />
    );
};
