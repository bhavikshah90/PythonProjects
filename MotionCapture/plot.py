from motion_capture import df

#import bokeh
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.models import HoverTool,ColumnDataSource



df["Start_String"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_String"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")
cds=ColumnDataSource(df)

#create figure object
f = figure(x_axis_type='datetime',height=100,width=500, sizing_mode='scale_width', title="Capture Motion Graph")
f.yaxis.minor_tick_line_color = None
f.ygrid[0].ticker.desired_num_ticks = 1
hover = HoverTool(tooltips=[("Start: ","@Start_String"),("End: ","@End_String")])
f.add_tools(hover)
# q = f.quad(left=df["Start"], right=df["End"],bottom=0,top=1,color="green")
q = f.quad(left="Start", right="End",bottom=0,top=1,color="green",source=cds) # after adding cds, we need not add df to take start end end field

#prepare output file
output_file("MotionGraph.html")
show(f)