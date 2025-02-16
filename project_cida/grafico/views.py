import plotly.graph_objects as go

from django.shortcuts import render


def sankey(request):
    fig = go.Figure(go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="black", width=0.5),
            label=["Entrada", "Processo A", "Processo B", "Saída"]
        ),
        link=dict(
            source=[0, 1, 1, 2],
            target=[1, 2, 3, 3],
            value=[10, 20, 30, 40]
        )
    ))

    graph_html = fig.to_html(full_html=False)

    return render(request, 'grafico/sankey.html', {'graph_html': graph_html})
