def render_taxis_list(taxis):
    return [
        {
            "id":taxi.id,
            "chofer":taxi.chofer,
            "color":taxi.color,
            "frec":taxi.frec,
            "ingresos":taxi.ingresos,
        }
        for taxi in taxis
    ]
    
def render_taxis_detail(taxi):
    return {
            "id":taxi.id,
            "chofer":taxi.chofer,
            "color":taxi.color,
            "frec":taxi.frec,
            "ingresos":taxi.ingresos,
        }