# vsphere_ds_exporter
vSphere DataStore Exporter For Prometheus
### Data Format
example data:
curl [http://127.0.0.1:5000/metrics/](http://127.0.0.1:5000/metrics/), You'll see the data format like this:
```
# HELP vsphere_datastore_capacity datastore capacity
# TYPE vsphere_datastore_capacity gauge
vsphere_datastore_capacity_bytes{name="NYFCLOUD-TYPE03-VOL"} 1145414090752
vsphere_datastore_freespace_bytes{name="NYFCLOUD-TYPE03-VOL"} 150457024512
vsphere_datastore_uncommitted_bytes{name="NYFCLOUD-TYPE03-VOL"} 5498350192533
```
### License
MIT License. See the [LICENSE](https://github.com/xujpxm/vsphere_ds_exporter/blob/master/LICENSE) file for details.