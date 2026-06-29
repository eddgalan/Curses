import React, { useEffect, useRef, useState } from "react";
import type { ImgHTMLAttributes } from "react";

type LazyImageProps = { src: string, onLazyLoad?: (img: HTMLImageElement) => void; };
type ImageNative = ImgHTMLAttributes<HTMLImageElement>
type Props = LazyImageProps & ImageNative;

export const LazyImage = ({
        src,
        onLazyLoad,
        ...imgProps
    }: Props ): React.JSX.Element => {
    const node = useRef<HTMLImageElement>(null);
    const [imageSrc, setImageSrc] = useState<string>("data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==");

    useEffect(() => {
        const img = node.current;

        if (!img) return;

        // Create a new IntersectionObserver instance
        const observer = new IntersectionObserver(entries => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    setImageSrc(src);

                    if (typeof onLazyLoad === "function") {
                        onLazyLoad(img);
                    }

                    // observer.disconnect(); // Stop observing once the image is loaded
                }
            });
        });

        // Start observing the target node
        observer.observe(img);

        // Stop observing the target node
        return () => {
            observer.disconnect();
        }
    }, [src, onLazyLoad]);

    return (
        <img src={ imageSrc }
             ref={ node }
             alt={ imgProps.alt ?? "" }
             { ...imgProps }
        />
    );
};
