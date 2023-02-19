import { ApiClient } from './../javascript-client-generated/src/ApiClient.js';
import { SpeechesMetaDataApi } from './../javascript-client-generated/src/api/SpeechesMetaDataApi.js';
import { env } from '$env/dynamic/public'

export default class ChartService {
    #apiInstance;
    constructor() {
        const client = new ApiClient();
        client.basePath = env.PUBLIC_API_URL;
        this.#apiInstance = new SpeechesMetaDataApi(client);
    }
    fetchSpeechTypes(callback) {
        console.log("wenigstens die scheisse soll funktionierne")
        this.#apiInstance.apiSpeechesMetaDataGetTypeOfSpeechesCountListGet(null, (error, data, response) => {
            console.log("??")
            if (error) {
                console.error("api call failed.")
                console.error(error);
                return null;
            } else {
                console.error("api call sucess.")
                let parsedData = JSON.stringify(data)
                console.log('API called successfully. Returned data: ' + parsedData);
                callback(data);
            }
        });
    }


    async fetchSpeechMetaData(callback) {
        this.#apiInstance.apiSpeechesMetaDataGet((error, data, response) => {
            if (error) {
                console.error(error);
                return null;
            } else {
                let parsedData = JSON.stringify(data)
                console.log('API called successfully. Returned data: ' + parsedData);
                callback(parsedData);
            }
        });
    }
}

