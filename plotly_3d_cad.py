import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import numpy as np
import trimesh

# 讀取 .stl 文件
mesh = trimesh.load_mesh('/Users/huangyanwei/python training/show_3d/All.stl')

# 將 mesh 頂點和面提取出來
vertices = mesh.vertices
faces = mesh.faces

# 定義 Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='3d-graph'),
])

# 渲染 STL 文件為 3D 圖
@app.callback(
    Output('3d-graph', 'figure'),
    Input('3d-graph', 'id')
)
def update_graph(_):
    fig = go.Figure(data=[go.Mesh3d(
        x=vertices[:, 0],
        y=vertices[:, 1],
        z=vertices[:, 2],
        i=faces[:, 0],
        j=faces[:, 1],
        k=faces[:, 2],
        color='lightblue',
        opacity=0.50
    )])

    # 設置視角
    fig.update_layout(scene=dict(aspectmode='data'))
    return fig

# 啟動應用
if __name__ == '__main__':
    app.run_server(debug=True)
