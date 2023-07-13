Dataset **Strawberry dataset for object detection** can be downloaded in Supervisely format:

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/S/b/Ab/31jjnWPVuosgD88vPN6p6jBtWtBVFGebhzIxJAydWKo2nHKQhMGhbMf1hGbTcIJlUub8tR7O61yUCwArrMs9JnJtEFK7o8AwlNqn420WaHN32piKxWsHXCoSRP4y.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Strawberry dataset for object detection', dst_path='~/dtools/datasets/Strawberry dataset for object detection.tar')
```
The data in original format can be 🔗[downloaded here](https://zenodo.org/record/6126677/files/strawberries.zip?download=1)