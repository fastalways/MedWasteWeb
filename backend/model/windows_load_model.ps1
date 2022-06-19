echo 'Loading Model from https://assets.gezdev.com/model-ai/medical-waste/4G-EfficientNetB5-epoch2000.pb.zip'
$client = new-object System.Net.WebClient
$CUR_DIR = Get-Location
$client.DownloadFile("https://assets.gezdev.com/model-ai/medical-waste/4G-EfficientNetB5-epoch2000.pb.zip",($CUR_DIR.Path+"\4G-EfficientNetB5-epoch2000.pb.zip"))
echo 'Loading Model from https://assets.gezdev.com/model-ai/medical-waste/41CLASSES-EfficientNetB5-epoch2000.pb.zip'
$client.DownloadFile("https://assets.gezdev.com/model-ai/medical-waste/41CLASSES-EfficientNetB5-epoch2000.pb.zip",($CUR_DIR.Path+"\41CLASSES-EfficientNetB5-epoch2000.pb.zip"))
echo 'Model Unzipping..................'
Expand-Archive '4G-EfficientNetB5-epoch2000.pb.zip'
Expand-Archive '41CLASSES-EfficientNetB5-epoch2000.pb.zip'
echo ('Model Saved at ...' + $CUR_DIR.Path)
echo '++++++++++ [Load/Extract Model] Completed ++++++++++'