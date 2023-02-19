# WebApi.SpeechesMetaDataApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiSpeechesMetaDataGet**](SpeechesMetaDataApi.md#apiSpeechesMetaDataGet) | **GET** /api/SpeechesMetaData | 
[**apiSpeechesMetaDataGetTypeOfSpeechesCountListGet**](SpeechesMetaDataApi.md#apiSpeechesMetaDataGetTypeOfSpeechesCountListGet) | **GET** /api/SpeechesMetaData/getTypeOfSpeechesCountList | 
[**apiSpeechesMetaDataIdDelete**](SpeechesMetaDataApi.md#apiSpeechesMetaDataIdDelete) | **DELETE** /api/SpeechesMetaData/{id} | 
[**apiSpeechesMetaDataIdGet**](SpeechesMetaDataApi.md#apiSpeechesMetaDataIdGet) | **GET** /api/SpeechesMetaData/{id} | 
[**apiSpeechesMetaDataIdPut**](SpeechesMetaDataApi.md#apiSpeechesMetaDataIdPut) | **PUT** /api/SpeechesMetaData/{id} | 
[**apiSpeechesMetaDataPost**](SpeechesMetaDataApi.md#apiSpeechesMetaDataPost) | **POST** /api/SpeechesMetaData | 

<a name="apiSpeechesMetaDataGet"></a>
# **apiSpeechesMetaDataGet**
> [SpeechesMetaData] apiSpeechesMetaDataGet()



### Example
```javascript
import {WebApi} from 'web_api';

let apiInstance = new WebApi.SpeechesMetaDataApi();
apiInstance.apiSpeechesMetaDataGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[SpeechesMetaData]**](SpeechesMetaData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

<a name="apiSpeechesMetaDataGetTypeOfSpeechesCountListGet"></a>
# **apiSpeechesMetaDataGetTypeOfSpeechesCountListGet**
> [TypeOfSpeechCountDto] apiSpeechesMetaDataGetTypeOfSpeechesCountListGet(opts)



### Example
```javascript
import {WebApi} from 'web_api';

let apiInstance = new WebApi.SpeechesMetaDataApi();
let opts = { 
  'politicalParty': ["politicalParty_example"], // [String] | 
  'legislature': "legislature_example", // String | 
  'meetingNumber': 56, // Number | 
  'topNumber': "topNumber_example" // String | 
};
apiInstance.apiSpeechesMetaDataGetTypeOfSpeechesCountListGet(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **politicalParty** | [**[String]**](String.md)|  | [optional] 
 **legislature** | **String**|  | [optional] 
 **meetingNumber** | **Number**|  | [optional] 
 **topNumber** | **String**|  | [optional] 

### Return type

[**[TypeOfSpeechCountDto]**](TypeOfSpeechCountDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

<a name="apiSpeechesMetaDataIdDelete"></a>
# **apiSpeechesMetaDataIdDelete**
> apiSpeechesMetaDataIdDelete(id)



### Example
```javascript
import {WebApi} from 'web_api';

let apiInstance = new WebApi.SpeechesMetaDataApi();
let id = "id_example"; // String | 

apiInstance.apiSpeechesMetaDataIdDelete(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="apiSpeechesMetaDataIdGet"></a>
# **apiSpeechesMetaDataIdGet**
> SpeechesMetaData apiSpeechesMetaDataIdGet(id)



### Example
```javascript
import {WebApi} from 'web_api';

let apiInstance = new WebApi.SpeechesMetaDataApi();
let id = "id_example"; // String | 

apiInstance.apiSpeechesMetaDataIdGet(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 

### Return type

[**SpeechesMetaData**](SpeechesMetaData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

<a name="apiSpeechesMetaDataIdPut"></a>
# **apiSpeechesMetaDataIdPut**
> apiSpeechesMetaDataIdPut(id, opts)



### Example
```javascript
import {WebApi} from 'web_api';

let apiInstance = new WebApi.SpeechesMetaDataApi();
let id = "id_example"; // String | 
let opts = { 
  'body': new WebApi.SpeechesMetaData() // SpeechesMetaData | 
};
apiInstance.apiSpeechesMetaDataIdPut(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 
 **body** | [**SpeechesMetaData**](SpeechesMetaData.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/_*+json
 - **Accept**: Not defined

<a name="apiSpeechesMetaDataPost"></a>
# **apiSpeechesMetaDataPost**
> apiSpeechesMetaDataPost(opts)



### Example
```javascript
import {WebApi} from 'web_api';

let apiInstance = new WebApi.SpeechesMetaDataApi();
let opts = { 
  'body': new WebApi.SpeechesMetaData() // SpeechesMetaData | 
};
apiInstance.apiSpeechesMetaDataPost(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SpeechesMetaData**](SpeechesMetaData.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/_*+json
 - **Accept**: Not defined

