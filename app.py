import math
from datetime import datetime, timedelta
import random

import dash
from dash import Dash, dcc, html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

app: Dash = dash.Dash(__name__)
app.title = "Human Factor UI"


def _time_series_points(minutes: int = 60):
    base = datetime.now()
    times = [base - timedelta(minutes=m) for m in reversed(range(minutes))]
    values = [70 + 5 * math.sin(idx / 6) + random.uniform(-3, 3) for idx in range(minutes)]
    return pd.DataFrame({"time": times, "value": values})


def heart_rate_chart():
    df = _time_series_points(90)
    fig = px.line(df, x="time", y="value", markers=False)
    fig.update_traces(line_color="#3DDCFF", fill="tozeroy", fillcolor="rgba(61,220,255,0.15)")
    fig.update_layout(
        margin=dict(l=25, r=10, t=30, b=30),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#E0F7FF"),
        xaxis_title="时间",
        yaxis_title="心率 bpm",
        xaxis=dict(showgrid=True, gridcolor="rgba(61,220,255,0.2)"),
        yaxis=dict(showgrid=True, gridcolor="rgba(61,220,255,0.2)")
    )
    return fig


def space_heatmap():
    heat_data = [[random.uniform(0.1, 1.0) for _ in range(7)] for _ in range(5)]
    fig = go.Figure(data=go.Heatmap(
        z=heat_data,
        colorscale="Turbo",
        showscale=False
    ))
    fig.update_layout(
        margin=dict(l=25, r=10, t=20, b=25),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
    )
    return fig


def mood_chart():
    df = _time_series_points(30)
    fig = px.line(df, x="time", y="value", markers=True)
    fig.update_traces(line_color="#7DF9FF")
    fig.update_layout(
        margin=dict(l=25, r=10, t=20, b=30),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#E0F7FF"),
        xaxis=dict(showgrid=False, title="时间"),
        yaxis=dict(showgrid=True, gridcolor="rgba(255,255,255,0.1)", title="情绪指标"),
    )
    return fig


def behavior_chart():
    x_vals = [random.uniform(0, 100) for _ in range(40)]
    y_vals = [random.uniform(0, 100) for _ in range(40)]
    sizes = [random.uniform(8, 18) for _ in range(40)]
    fig = px.scatter(x=x_vals, y=y_vals, size=sizes, color=sizes,
                     color_continuous_scale="icefire")
    fig.update_layout(
        margin=dict(l=25, r=10, t=20, b=25),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#E0F7FF"),
        xaxis=dict(showgrid=True, gridcolor="rgba(61,220,255,0.1)", title="X"),
        yaxis=dict(showgrid=True, gridcolor="rgba(61,220,255,0.1)", title="Y"),
        showlegend=False,
    )
    return fig


def radar_chart():
    categories = ["反应速度", "情绪稳定", "沟通协作", "执行力", "注意力"]
    values = [8.2, 7.5, 8.8, 7.9, 8.1]
    angles = values + values[:1]
    labels = categories + categories[:1]
    fig = go.Figure(data=go.Scatterpolar(r=angles, theta=labels, fill='toself', line_color="#3DDCFF"))
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 10], gridcolor="rgba(61,220,255,0.2)")),
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#E0F7FF"),
        margin=dict(l=25, r=10, t=20, b=20)
    )
    return fig


def stacked_area_chart():
    times = pd.date_range(datetime.now() - timedelta(hours=6), periods=50, freq="7min")
    df = pd.DataFrame({
        "time": times,
        "技能": [40 + 5 * math.sin(i / 8) + random.uniform(-5, 5) for i in range(len(times))],
        "情绪": [30 + 4 * math.cos(i / 7) + random.uniform(-4, 4) for i in range(len(times))],
        "警觉度": [25 + 6 * math.sin(i / 5) + random.uniform(-3, 3) for i in range(len(times))],
        "疲劳": [15 + 3 * math.cos(i / 4) + random.uniform(-2, 2) for i in range(len(times))],
    })
    fig = px.area(df, x="time", y=["技能", "情绪", "警觉度", "疲劳"], color_discrete_sequence=px.colors.sequential.Tealgrn)
    fig.update_layout(
        margin=dict(l=25, r=10, t=20, b=30),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#E0F7FF"),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    return fig


def bar_pillars():
    groups = ["人因分析", "综合指数", "情绪指数", "感知指数"]
    scores = [88, 84, 90, 82]
    fig = go.Figure(go.Bar(
        x=scores,
        y=groups,
        orientation='h',
        marker=dict(color=["#3DDCFF", "#80D7FF", "#5EF0CF", "#59B1FF"]),
        text=[f"{s}%" for s in scores],
        textposition='inside'
    ))
    fig.update_layout(
        margin=dict(l=25, r=10, t=20, b=20),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#E0F7FF"),
        xaxis=dict(showgrid=False, range=[0, 100]),
        yaxis=dict(showgrid=False)
    )
    return fig


card_block = html.Div(
    className="panel card",
    children=[
        html.Div(className="panel-title", children="人因信息展示"),
        html.Div(
            className="card-body",
            children=[
                html.Div(
                    className="avatar-panel",
                    children=[
                        html.Div(className="avatar-outline"),
                        html.Div(className="tag-list", children=[html.Div(tag, className="tag") for tag in ["指纹", "虹膜", "光学"]]),
                        html.Div(className="state-label", children="正常进入人数: 1人"),
                    ],
                ),
                html.Div(
                    className="vitals-panel",
                    children=[
                        html.Div(
                            className="sensor",
                            children=[
                                html.Div("体温检测", className="sensor-title"),
                                html.Div(["正常: ", html.Span("正常")], className="sensor-value"),
                                html.Div("体温 -36°左右", className="sensor-desc"),
                            ],
                        ),
                        html.Div(
                            className="sensor", children=[
                                html.Div("呼吸监测", className="sensor-title"),
                                html.Div(["正常: ", html.Span("正常")], className="sensor-value"),
                                html.Div("呼吸频率正常", className="sensor-desc"),
                            ]),
                        html.Div(
                            className="sensor", children=[
                                html.Div("血压监测", className="sensor-title"),
                                html.Div(["正常: ", html.Span("正常")], className="sensor-value"),
                                html.Div("血压正常(高低血压)", className="sensor-desc"),
                            ]),
                    ],
                ),
            ],
        ),
    ],
)


info_grid = html.Div(
    className="grid",
    children=[
        html.Div(className="panel", children=[html.Div("空间分布", className="panel-title"), dcc.Graph(figure=space_heatmap(), config={"displayModeBar": False})]),
        html.Div(className="panel", children=[html.Div("情绪状态展示", className="panel-title"), dcc.Graph(figure=mood_chart(), config={"displayModeBar": False})]),
        html.Div(className="panel", children=[html.Div("状态监测", className="panel-title"), dcc.Graph(figure=behavior_chart(), config={"displayModeBar": False})]),
        html.Div(className="panel wide", children=[html.Div("行为轨迹", className="panel-title"), dcc.Graph(figure=behavior_chart(), config={"displayModeBar": False})]),
    ],
)


analysis_grid = html.Div(
    className="grid",
    children=[
        html.Div(className="panel", children=[html.Div("心率", className="panel-title"), dcc.Graph(figure=heart_rate_chart(), config={"displayModeBar": False})]),
        html.Div(className="panel", children=[html.Div("精神状态", className="panel-title"), dcc.Graph(figure=radar_chart(), config={"displayModeBar": False})]),
        html.Div(className="panel", children=[html.Div("人因组合分析", className="panel-title"), dcc.Graph(figure=stacked_area_chart(), config={"displayModeBar": False})]),
        html.Div(className="panel", children=[html.Div("感知能力", className="panel-title"), dcc.Graph(figure=bar_pillars(), config={"displayModeBar": False})]),
    ],
)


app.layout = html.Div(
    className="app",
    children=[
        html.Div(className="hero-title", children="人因信息展示"),
        html.Div(
            className="section",
            children=[card_block, info_grid],
        ),
        html.Div(className="hero-title", children="人因分析系统"),
        html.Div(
            className="section",
            children=[analysis_grid],
        ),
    ],
)


if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8050, debug=False)
