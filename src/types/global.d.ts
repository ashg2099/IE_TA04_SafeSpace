// Providing type declarations for Mapbox
interface MapboxGl {
    Map: any;
    Popup: any;
    accessToken: string;
    [key: string]: any;
}

declare global {
    interface Window {
        mapboxgl: MapboxGl;
    }
}

// Provide type declarations for resource files
declare module '*.svg' {
    const value: string;
    export default value;
}

declare module '*.jpg' {
    const value: string;
    export default value;
}

export { };