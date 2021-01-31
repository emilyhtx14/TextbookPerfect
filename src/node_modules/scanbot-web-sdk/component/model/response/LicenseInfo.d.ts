export declare class LicenseInfo {
    status: string;
    description: string;
    isValid(): boolean;
    static fromJson(json: any): LicenseInfo;
}
