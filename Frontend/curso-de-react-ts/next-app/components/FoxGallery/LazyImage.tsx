import React, { useEffect, useRef, useState } from "react";
import type { ImgHTMLAttributes } from "react";

type LazyImageProps = { src: string };
type ImageNative = ImgHTMLAttributes<HTMLImageElement>
type Props = LazyImageProps & ImageNative;

export const LazyImage = ({ src, ...imgProps }: Props ): React.JSX.Element => {
    const node = useRef<HTMLImageElement>(null);
    const [imageSrc, setImageSrc] = useState<string>("data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==");

    useEffect(() => {
        if (!node.current) return;

        // Create a new IntersectionObserver instance
        const observer = new IntersectionObserver(entries => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    setImageSrc(src);
                }
            });
        });

        // Start observing the target node
        observer.observe(node.current);

        // Stop observing the target node
        return () => {
            observer.disconnect();
        }
    }, [imageSrc]);

    return (
        <img src={ src }
             ref={ node }
             { ...imgProps }
        />
    );
};
