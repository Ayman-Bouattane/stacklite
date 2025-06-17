import React from 'react';
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';

export default function TopTags({ data }) {
  const chartData = Object.entries(data).map(([tag, count]) => ({ tag, count }));

  return (
    <div className="mb-8">
      <h2 className="text-xl mb-2">Top 10 Tags</h2>
      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={chartData}>
          <XAxis dataKey="tag" />
          <YAxis />
          <Tooltip />
          <Bar dataKey="count" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}