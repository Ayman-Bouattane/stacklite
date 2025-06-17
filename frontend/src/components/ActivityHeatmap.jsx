import React from 'react';
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';

export default function ActivityHeatmap({ data }) {
  const chartData = Object.entries(data).map(([ym, count]) => ({ date: ym, count }));

  return (
    <div className="mb-8">
      <h2 className="text-xl mb-2">Monthly Activity</h2>
      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={chartData}>
          <XAxis dataKey="date" />
          <YAxis />
          <Tooltip />
          <Line dataKey="count" />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}