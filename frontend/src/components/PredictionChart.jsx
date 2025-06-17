import React from 'react';
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';

export default function PredictionChart({ data }) {
  return (
    <div className="mb-8">
      <h2 className="text-xl mb-2">Posts Prediction (Next Days)</h2>
      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={data}>
          <XAxis dataKey="date" />
          <YAxis />
          <Tooltip />
          <Line dataKey="predicted" />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}