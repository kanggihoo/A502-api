# 01-Report client performance metrics [POST]

`POST /api/v4/client_perf`

Uploads client performance measurements to the server as part of the Client Performance Monitoring feature.
__Minimum server version__: 9.9.0


### Request Body (application/json)

```json
{
  "version": string (required), // An identifier for the schema of the data being submitted which currently must be "0.1.0"
  "client_id": string, // Not currently used
  "labels": [
    string
  ], // Labels to be applied to all metrics when recorded by the metrics backend
  "start": integer (required), // The time in milliseconds of the first metric in this report
  "end": integer (required), // The time in milliseconds of the last metric in this report
  "counters": [
    {
      "metric": string (required), // The name of the counter
      "value": number (required), // The value to increment the counter by
      "timestamp": integer, // The time that the counter was incremented
      "labels": [
        string
      ], // Labels to be applied to this metric when recorded by the metrics backend
    }
  ], // An array of counter metrics to be reported
  "histograms": [
    {
      "metric": string (required), // The name of the measurement
      "value": number (required), // The value of the measurement
      "timestamp": integer, // The time that the measurement was taken
      "labels": [
        string
      ], // Labels to be applied to this metric when recorded by the metrics backend
    }
  ], // An array of histogram measurements to be reported
}
```
### Responses

#### 200 - Measurements reported successfully

Schema (application/json):
```json
{
  "status": string, // Will contain "ok" if the request was successful and there was nothing else to return
}
```

#### 400 - 

#### 401 - 

#### 403 - 

#### 500 - 

