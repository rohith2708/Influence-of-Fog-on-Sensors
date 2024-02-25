# Influence-of-Fog-on-Sensors
The objective of this analysis is to evaluate the influence of fog on the point cloud data of the Lidar and Radar sensors by comparing their measurements of their distance in clear and foggy conditions.
The objective of this analysis is to evaluate the influence of fog on the point cloud data of
the Lidar and Radar sensors by comparing their measurements of their distance in clear and
foggy conditions. From the provided recordings of these sensor point cloud data, we will be
utilizing the 3D coordinates x,y and z to arrive at the distance for these points with respect
to the origin.
Each point in our sensor point cloud recordings corresponds to a location in three-dimensional
space. The coordinates (X, Y, Z) represent the point’s position in a Cartesian coordinate
system. The distance from the origin to each point in the point cloud is calculated using the
Euclidean distance formula
Distance =
p
x2 + y2 + z2 [m]
Using the histogram plot, we are making a statistical analysis of the fog and no-fog influences
on the point cloud data of the sensors. ”bin” is a parameter in ”matplotlib.pyplot.hist(),”
which impacts the visualization of the histogram. Bin determines the intervals into which
the data will be divided. We have taken bins = 40 and range = [0, 40]. These values were
chosen so as to get a plot covering a wide range of distances, which helped us provide a
more detailed plot.
5.1 Blickfeld Cube 1 Sensor
From figures 1 and 2, we observe that, between the distances of 0–5 units, there is a spike in
the range of the number of points. This is due to the fact that the Blickfeld Cube 1 produces
a scan line for the close proximity range. In the fog condition, due to denser fog, the laser
points emitted tend to make multiple reflections, producing much more point generation at
this close proximity range. Beyond the distance of 15.6 units, we see a loss of plenty of
points since the maximal viewing distance is limited under fog when compared to the clear
weather capabilities.
5.2 VelodynePuck Sensor
From figures 3 and 4, it is clear that, at a short distance range of 0–5 units, there is a
smaller loss in the overall point cloud distribution. This may be due to the fact that the
laser scattering is having little impact at this short-distance range. At the medium-distance
range of 7 units, the scattering of laser beams due to fog becomes more intense, leading to a
drop in the intensity of the points. However, at distances more than 6 units, we see a drop
in the intensity of the number of points, and beyond 15 units, there is a huge loss of points.
Thus, with VelodynePuck’s long-distance range, fog plays a dramatic role.
5.3 Texas Instruments MMWCAS-RF-EVM: Radar Sensor
Radar waves have longer wavelengths, making them less vulnerable to scattering and absorption
by fog particles when compared to Lidar. Observe figures 5 and 6. Some degree of
dispersion and absorption still occurs, say, in the short and mid range distances between 0
and 5 units. The loss of points at these ranges might be a result of the subtle interactions
between radar signals and fog particles, as well as fluctuations in environmental conditions.
