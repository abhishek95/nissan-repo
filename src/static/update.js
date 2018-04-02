function update_values() {
            $SCRIPT_ROOT = {{ request.script_root|tojson|safe }};
            $.getJSON($SCRIPT_ROOT+"/loc",
                function(data) {
                    $("#lat").text(data.lat)
                    $("#lon").text(data.lon)
                });
        }
        
        